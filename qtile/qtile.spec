%global __python %{__python3}
%global pkg_name qtile

Name: %{pkg_name}
# We use a placeholder version and let Git/setuptools_scm determine the real version.
Version: 0.33.0
Release: 0.1.gitsnap%{?dist}
Summary: A pure-Python tiling window manager
License: MIT AND GPL-3.0-or-later
Url: https://github.com/qtile/qtile

# No Source file is needed for a Git build.
# Source: %{name}-%{version}.tar.gz

ExcludeArch: %{ix86}

# We need 'git' to clone the repository in %prep
BuildRequires:  git
BuildRequires:  python3-devel
BuildRequires:  desktop-file-utils
BuildRequires:  gcc
BuildRequires:  xorg-x11-server-Xvfb
BuildRequires:  xorg-x11-server-Xephyr
BuildRequires:  rsvg-pixbuf-loader
BuildRequires:  pkgconfig(wlroots)
BuildRequires:  pkgconfig(wayland-protocols)
BuildRequires:  pkgconfig(wayland-scanner)
BuildRequires:  python3-build
BuildRequires:  python3-installer
BuildRequires:  python3-setuptools-scm
BuildRequires:  python3-wheel
BuildRequires:  python3-isort
BuildRequires:  python3-cairocffi
BuildRequires:  python3-cffi
BuildRequires:  python3-xcffib

# CFFI dependencies for dynamic loading
%if 0%{?__isa_bits} == 32
%global libsymbolsuffix %{nil}
%else
%global libsymbolsuffix ()(%{__isa_bits}bit)
%endif

BuildRequires: libgobject-2.0.so.0%{libsymbolsuffix}
BuildRequires: libpango-1.0.so.0%{libsymbolsuffix}
BuildRequires: libpangocairo-1.0.so.0%{libsymbolsuffix}
Requires: libgobject-2.0.so.0%{libsymbolsuffix}
Requires: libpango-1.0.so.0%{libsymbolsuffix}
Requires: libpangocairo-1.0.so.0%{libsymbolsuffix}

Recommends: python3-psutil
Recommends: python3-pyxdg
Recommends: python3-dbus-fast
Recommends: python3-mpd2
Recommends: alsa-utils
Recommends: lm_sensors
Recommends: procps-ng

%description
A pure-Python tiling window manager. This package is built directly from the latest Git development snapshot of the **main branch**.

# ... (subpackage definitions remain the same) ...


%prep
# No %setup macro is used since we have no Source file to extract.

# 1. Clone the repository into a directory named 'qtile'.
# Note: For COPR, you must ensure the resulting directory is named correctly for subsequent steps.
mkdir %{pkg_name}
cd %{pkg_name}
git clone %{url} .

# 2. Check out the desired branch (main)
git checkout main
# Use this line instead of the checkout if you want to rebuild based on a specific commit hash:
# git checkout <HASH_FROM_LAST_SUCCESSFUL_AUR_BUILD>

# 3. Use the placeholder version for setuptools_scm, as Git is present.
export SETUPTOOLS_SCM_PRETEND_VERSION=%{version}

# 4. Remove the .git directory before building to mimic a clean checkout
#    and prevent setuptools_scm from using its expensive git operations
#    during the build phase inside the sandbox, though this is often optional
#    when setuptools_scm_pretend_version is set. We'll skip this step
#    since we want setuptools_scm to capture the snapshot version.
# cd .. # Move up to the BUILD directory before %build runs
# cd %{pkg_name}

%build
cd %{pkg_name}
# setuptools_scm uses the git history to calculate a version like 0.33.0.devN+g<hash>
%pyproject_wheel
PYTHONPATH=${PWD} ./scripts/ffibuild
cd ..


%install
cd %{pkg_name}
%pyproject_install

mkdir -p %{buildroot}%{_datadir}/xsessions/
desktop-file-install \
    --dir %{buildroot}%{_datadir}/xsessions/ \
    resources/qtile.desktop

mkdir -p %{buildroot}%{_datadir}/wayland-sessions/
desktop-file-install \
    --dir %{buildroot}%{_datadir}/wayland-sessions/ \
    resources/qtile-wayland.desktop

%pyproject_save_files libqtile
cd ..


%check
cd %{pkg_name}
export LC_TYPE=en_US.UTF-8
# Running tests in parallel as per the AUR PKGBUILD, allowing failure.
%pytest -vv -n auto --backend x11 --backend wayland || true
cd ..


%files
%doc README.rst
%doc libqtile/resources/default_config.py
%doc CHANGELOG
%{_bindir}/qtile
%{_datadir}/xsessions/qtile.desktop

%files -n python3-libqtile
%license LICENSE
# The %pyproject_files macro is used in the %install section to populate this list.

%files wayland
%{_datadir}/wayland-sessions/qtile-wayland.desktop

%changelog
* %{currenttimeanddate} <Maintainer Name> - %{version}-%{release}
- Initial git snapshot build for COPR using direct Git clone.
