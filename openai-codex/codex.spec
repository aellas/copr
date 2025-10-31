%global crate codex-rs
%global pkg_name openai-codex
%global rust_tag rust-v

Name:           %{pkg_name}
Version:        0.52.0
Release:        1%{?dist}
Summary:        Lightweight coding agent that runs in your terminal
License:        Apache-2.0
URL:            https://github.com/openai/codex
Source0:        %{url}/archive/refs/tags/%{rust_tag}%{version}.tar.gz

Requires:       openssl
Requires:       gcc-libs
Requires:       glibc

BuildRequires:  cargo
BuildRequires:  rust
BuildRequires:  pkgconfig
BuildRequires:  make

BuildRequires:  openssl-devel
BuildRequires:  gcc

%description
Lightweight coding agent that runs in your terminal.

%prep
%setup -q -n codex-%{rust_tag}%{version}

cd codex-rs

%build
export RUSTUP_TOOLCHAIN=stable
export CARGO_TARGET_DIR=target

cargo build --release

%install
mkdir -p %{buildroot}%{_bindir}

mkdir -p %{buildroot}%{_licensedir}/%{name}

install -m 0755 target/release/codex %{buildroot}%{_bindir}/
install -m 0755 target/release/codex-exec %{buildroot}%{_bindir}/
install -m 0755 target/release/codex-linux-sandbox %{buildroot}%{_bindir}/
install -m 0644 LICENSE %{buildroot}%{_licensedir}/%{name}

%files
%license LICENSE
%{_bindir}/codex
%{_bindir}/codex-exec
%{_bindir}/codex-linux-sandbox

%changelog
* %{date} Christopher Cooper - %{version}-1
- Initial Fedora packaging based on Arch PKGBUILD.
