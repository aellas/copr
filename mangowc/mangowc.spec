%global forgeurl https://github.com/DreamMaoMao/mangowc
%global version 0.10.6

Name:           mangowc
Version:        %{version}
Release:        1%{?dist}
Summary:        Lightweight Wayland compositor with smooth animation

License:        GPL-3.0-or-later
URL:            %{forgeurl}
Source0:        %{forgeurl}/archive/refs/tags/%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  meson
BuildRequires:  ninja-build
BuildRequires:  pkgconfig
BuildRequires:  wayland-devel
BuildRequires:  wayland-protocols-devel
BuildRequires:  wlroots-devel
BuildRequires:  libinput-devel
BuildRequires:  libdrm-devel
BuildRequires:  libxkbcommon-devel
BuildRequires:  pixman-devel
BuildRequires:  libseat-devel
BuildRequires:  pcre2-devel
BuildRequires:  scenefx-devel

Requires:       scenefx

%description
MangoWC is a lightweight Wayland compositor based on wlroots and SceneFX.
It provides smooth animations, multiple layouts, and modern input support.

%prep
%autosetup -n %{name}-%{version}

%build
%meson -Dxwayland=enabled
%meson_build

%install
%meson_install

# Remove upstream-installed files we replace (if they exist)
rm -f %{buildroot}/etc/mango/config.conf || :
rm -f %{buildroot}%{_datadir}/wayland-sessions/mango.desktop || :

# Install corrected session desktop entry
install -Dm0644 mango.desktop %{buildroot}%{_datadir}/wayland-sessions/mango.desktop

# Install default config in correct location
mkdir -p %{buildroot}%{_sysconfdir}/mango
install -Dm0644 config.conf %{buildroot}%{_sysconfdir}/mango/config.conf

%files
%license LICENSE*
%doc README.md
%{_bindir}/mango
%{_bindir}/mmsg
%{_datadir}/wayland-sessions/mango.desktop
%config(noreplace) %{_sysconfdir}/mango/config.conf

%changelog
* Sat Nov 29 2025 Zac <zacpi@pm.me> - 0.10.6
- Build from tag v0.10.6
* Fri Nov 07 2025 Christian Bendiksen <christian@bendiksen.me> - 0.10.5-1
- Build from stable upstream tag v0.10.5
