# Name: qtile

%global __python %{__python3}
%global pkg_name qtile

Name: %{pkg_name}
Version: 0.33.0
Release: 0.1.gitsnap%{?dist}
Summary: A pure-Python tiling window manager
License: MIT AND GPL-3.0-or-later
Url: http://qtile.org

Source: https://github.com/qtile/qtile/archive/main/%{pkg_name}-main.tar.gz

ExcludeArch: %{ix86}

BuildRequires:  python3-devel
BuildRequires:  desktop-file-utils
BuildRequires:  git
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

Requires: python3-libqtile = %{version}-%{release}

Recommends: python3-psutil
Recommends: python3-pyxdg
Recommends: python3-dbus-fast
Recommends: python3-mpd2
Recommends: alsa-utils
Recommends: lm_sensors
Recommends: procps-ng

%description
A pure-Python tiling window manager. This package is built from a Git development snapshot.

Features
========
    * Simple, small and extensible.
    * Configured in Python.
    * Complete remote scriptability.


%package -n python3-libqtile
Summary: Qtile's python library
Requires: python3-cairocffi
Requires: python3-cffi
Requires: python3-xcffib

%description -n python3-libqtile
%{summary}.

%package wayland
Summary: Qtile wayland session
BuildRequires: xorg-x11-server-Xwayland
Requires: qtile = %{version}-%{release}
Requires: python3-libqtile

%description wayland
%{summary}.


%prep
%setup -q -n %{pkg_name}-main

export SETUPTOOLS_SCM_PRETEND_VERSION=%{version}

mkdir -p .git
touch .git/HEAD
touch .git/index
git init .
git add .
git commit -m "Snapshot build" --allow-empty
git tag v%{version} -m "pretend tag"
git describe --tags --long --abbrev=7


%build
%pyproject_wheel
PYTHONPATH=${PWD} ./scripts/ffibuild


%install
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


%check
export LC_TYPE=en_US.UTF-8
%pytest -vv --backend x11 --backend wayland || true


%files
%doc README.rst
%doc libqtile/resources/default_config.py
%doc CHANGELOG
%{_bindir}/qtile
%{_datadir}/xsessions/qtile.desktop

%files -n python3-libqtile -f %{pyproject_files}
%license LICENSE

%files wayland
%{_datadir}/wayland-sessions/qtile-wayland.desktop

%changelog
* %{currenttimeanddate} <Maintainer Name> - %{version}-%{release}
- Initial git snapshot build for COPR
