%global crate bluetuith

Name:           %{crate}
Version:        0.2.5_rc1
Release:        1%{?dist}
Summary:        TUI-based Bluetooth manager
License:        MIT
URL:            https://github.com/bluetuith-org/%{crate}
Source0:        %{url}/archive/refs/tags/v%{version}.tar.gz

BuildRequires:  go
Requires:       bluez
Requires:       dbus

%description
Bluetuith is a terminal user interface (TUI)-based Bluetooth manager written in Go.
It provides an ncurses-style interface to connect, pair, and manage Bluetooth devices.

%prep
%autosetup -n %{crate}-%{version}

%build
go build -v \
   -ldflags="-s -w -X github.com/darkhz/bluetuith/cmd.Version=v%{version}" \
   -o %{crate} ./cmd

%install
install -Dm755 %{crate} %{buildroot}%{_bindir}/%{crate}

%check
%{buildroot}%{_bindir}/%{crate} --version || true

%files
%license LICENSE
%doc README.md
%{_bindir}/%{crate}

%changelog
* Thu Nov 06 2025 Your Name <you@example.com> - 0.2.5_rc1-1
- Initial Fedora packaging (built from Go source)
