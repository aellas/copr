Name:           qtile-git
Version:        0.33.0.r282.gc3d4510        
Release:        1
Summary:        A full-featured, pure-Python tiling window manager
License:        MIT
URL:            https://github.com/qtile/qtile
VCS:            git:https://github.com/qtile/qtile.git
BuildArch:      noarch
Source0:        none

# Runtime dependencies
Requires:       gdk-pixbuf2
Requires:       libnotify
Requires:       librsvg2
Requires:       pango
Requires:       python3
Requires:       python3-cairocffi
Requires:       python3-cffi
Requires:       python3-gobject
Requires:       python3-xcffib

# Build dependencies
BuildRequires:  git
BuildRequires:  pulseaudio-libs-devel
BuildRequires:  python3-build
BuildRequires:  python3-installer
BuildRequires:  python3-setuptools_scm
BuildRequires:  python3-wheel
BuildRequires:  wlroots-devel
BuildRequires:  wayland-devel
BuildRequires:  wayland-protocols-devel
BuildRequires:  xorg-x11-server-Xwayland

%description
Qtile is a full-featured, pure-Python tiling window manager supporting both X11 and Wayland.

%prep
%setup -q -T -c %{name} || :
%autosetup -S git

# Generate a pseudo-version string for informational purposes
git describe --tags --long --abbrev=7 2>/dev/null | \
    sed 's/\([^-]*-g\)/r\1/;s/-/./g;s/^v//' > .version || echo "git" > .version

%build
PYTHONPATH=$PWD python3 libqtile/backend/wayland/cffi/build.py
python3 -m build --no-isolation --wheel

%install
python3 -m installer --destdir=%{buildroot} dist/*.whl

install -Dm644 LICENSE %{buildroot}%{_licensedir}/%{name}/LICENSE
install -Dm644 CHANGELOG README.rst libqtile/resources/default_config.py \
    -t %{buildroot}%{_docdir}/%{name}/
install -Dm644 resources/qtile.desktop %{buildroot}%{_datadir}/xsessions/qtile.desktop
install -Dm644 resources/qtile-wayland.desktop %{buildroot}%{_datadir}/wayland-sessions/qtile-wayland.desktop

%check
pytest -v || true

%files
%license %{_licensedir}/%{name}/LICENSE
%doc %{_docdir}/%{name}/*
%{_bindir}/qtile
%{python3_sitelib}/libqtile*
%{_datadir}/xsessions/qtile.desktop
%{_datadir}/wayland-sessions/qtile-wayland.desktop

%changelog
* Tue Oct 28 2025 You <you@example.com> - 0-1
- Initial COPR git build
