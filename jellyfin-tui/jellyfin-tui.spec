%global crate jellyfin-tui

Name:           %{crate}
Version:        1.3.0
Release:        1%{?dist}
Summary:        Music streaming TUI client for Jellyfin

License:        GPL-3.0-only
URL:            https://github.com/dhonus/%{name}

Source0:        %{url}/archive/v%{version}.tar.gz

Requires:       mpv
Requires:       openssl
Requires:       sqlite

BuildRequires:  cargo
BuildRequires:  rust
BuildRequires:  pkgconfig
BuildRequires:  make

BuildRequires:  mpv-devel
BuildRequires:  openssl-devel
BuildRequires:  sqlite-devel

%description
A feature-rich, music streaming Terminal User Interface (TUI) client for Jellyfin.

%prep
%autosetup -n %{crate}-%{version}

%build
export LIBSQLITE3_SYS_USE_PKG_CONFIG=1
export PKG_CONFIG_ALLOW_CROSS=1

cargo build --release

%install
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_docdir}/%{name}
mkdir -p %{buildroot}%{_licensedir}/%{name}
mkdir -p %{buildroot}%{_datadir}/applications

install -m 0755 target/release/%{name} %{buildroot}%{_bindir}/%{name}

install -m 0644 README.md %{buildroot}%{_docdir}/%{name}

install -m 0644 LICENSE %{buildroot}%{_licensedir}/%{name}

install -m 0644 src/extra/jellyfin-tui.desktop \
    %{buildroot}%{_datadir}/applications/%{name}.desktop

%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop

%changelog
* %{date} %{user} - 1.2.6-1
- Initial Fedora packaging.
* %{date} %{user} -  1.3.0-1
- https://github.com/dhonus/jellyfin-tui/releases/tag/v1.3.0
