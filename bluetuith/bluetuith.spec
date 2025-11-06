Name:           bluetuith
Version:        0.2.5
Release:        0
Summary:        A TUI bluetooth manager for Linux
License:        MIT
URL:            https://github.com/darkhz/bluetuith
Source:         %{name}-%{version}.tar.gz
BuildRequires:  golang-packaging
Requires:       bluez
Requires:       dbus-1

%description
bluetuith is a TUI-based bluetooth connection manager, which can interact with bluetooth adapters and devices. It aims to be a replacement to most bluetooth managers, like blueman.
This project is currently in the alpha stage.

%prep
%setup -q -a 1

%build
go build \
   -mod=vendor \
   -buildmode=pie

%install
install -D -m0755 %{name} %{buildroot}%{_bindir}/%{name}

%files
%{_bindir}/%{name}

%changelog
