Name:           bluetuith
Version:        0.2.5_rc1
Release:        1%{?dist}
Summary:        A TUI bluetooth manager for Linux
License:        MIT
URL:            https://github.com/bluetuith-org/bluetuith
Source0:        https://github.com/bluetuith-org/bluetuith/releases/download/v0.2.5-rc1/bluetuith_0.2.5-rc1_Linux_x86_64.tar.gz
BuildArch:      x86_64
Requires:       bluez
Requires:       dbus

%description
bluetuith is a TUI-based Bluetooth manager for Linux with a terminal interface.

%prep
mkdir -p %{crate}-%{version}
tar -xzf %{SOURCE0} -C %{crate}-%{version}

%build

%install
install -Dm755 %{crate}-%{version}/bluetuith %{buildroot}%{_bindir}/bluetuith
install -Dm644 %{crate}-%{version}/LICENSE %{buildroot}%{_licensedir}/bluetuith/LICENSE

%files
%{_bindir}/bluetuith
%license %{_licensedir}/bluetuith/LICENSE

%changelog
* Thu Nov 06 2025 lxdes zacpi@pm.me - 0.2.5-1
- Initial COPR packaging from binary release
