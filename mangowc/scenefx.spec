%global forgeurl https://github.com/DreamMaoMao/scenefx
%global branch   main

Name:           scenefx
Version:        0
Release:        0.1.%{branch}%{?dist}
Summary:        Effects library for wlroots Wayland compositors

License:        GPL-3.0-or-later
URL:            %{forgeurl}
# Download the branch tarball and rename it to a stable filename
Source0:        %{forgeurl}/archive/refs/heads/%{branch}.tar.gz#/%{name}-%{branch}.tar.gz

BuildRequires:  meson
BuildRequires:  gcc
BuildRequires:  gcc-c++
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

Requires:       wlroots

%description
SceneFX provides advanced animation and visual effects for wlroots Wayland
compositors.

%package devel
Summary: Development files for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
Headers and pkgconfig files needed to develop software using SceneFX.

%prep
%autosetup -n %{name}-%{branch}

%build
%meson -Dexamples=false
%meson_build

%install
%meson_install

find %{buildroot} -name '*.la' -delete || :

%files
%license LICENSE*
%doc README.md
%{_libdir}/libscenefx-0.4.so*

%files devel
%{_includedir}/scenefx-0.4/
%{_libdir}/pkgconfig/scenefx-0.4.pc

%changelog
* Thu Nov 06 2025 Christian Bendiksen <christian@bendiksen.me> - 0-0.1.main
- Git branch snapshot packaging (no git macros)
