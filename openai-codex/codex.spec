%global pkg_name openai-codex
%global rust_tag rust-v
%global crate_dir codex-rs
%global tarball_name codex-%{rust_tag}%{version}

Name:           %{pkg_name}
Version:        0.53.0
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

%undefine _lto_cflags

%description
Lightweight coding agent that runs in your terminal. This package uses the Rust
implementation of the OpenAI Codex agent.

%prep
%setup -q -n %{tarball_name}

%build
pushd %{crate_dir}

export RUSTUP_TOOLCHAIN=stable
export CARGO_TARGET_DIR=target

cargo build --release 

popd

%install
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_licensedir}/%{name}

install -m 0755 %{crate_dir}/target/release/codex %{buildroot}%{_bindir}/
install -m 0755 %{crate_dir}/target/release/codex-exec %{buildroot}%{_bindir}/
install -m 0755 %{crate_dir}/target/release/codex-linux-sandbox %{buildroot}%{_bindir}/

install -m 0644 %{crate_dir}/LICENSE %{buildroot}%{_licensedir}/%{name}

%files
%license %{_licensedir}/%{name}/LICENSE
%{_bindir}/codex
%{_bindir}/codex-exec
%{_bindir}/codex-linux-sandbox

%changelog
* Fri Oct 31 2025 LXDE  <zacpi@pm.me> - 0.53.0-1
- Initial Fedora packaging.
