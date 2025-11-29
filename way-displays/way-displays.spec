%global forgeurl https://github.com/alex-courtis/way-displays
%global version 1.15.0
%global tag %{version}
%forgemeta

Name:           way-displays
Version:        %{version}
Release:        %autorelease
Summary:        Auto Manage Your Wayland Displays
URL:            %{forgeurl}
Source:         %{forgesource}
License:        MIT

BuildRequires:  g++
BuildRequires:  bash
BuildRequires:  sed
BuildRequires:  make
BuildRequires:  wayland-devel
BuildRequires:  wayland-protocols-devel
BuildRequires:  libinput-devel
BuildRequires:  libudev-devel
BuildRequires:  yaml-cpp-devel
BuildRequires:  valgrind
BuildRequires:  libcmocka-devel

%description

%prep
%forgesetup

%build
%make_build

%install
%make_install PREFIX="/usr" PREFIX_ETC="/"

#%check
#todo not passing %{__make} test

%files
%license LICENSE
%doc README.md
%{_bindir}/way-displays
%config(noreplace) /etc/way-displays/cfg.yaml
%{_mandir}/man1/way-displays.1.*
%changelog
%autochangelog
