# Generated by rust2rpm 27
%bcond check 1
%global debug_package %{nil}

# prevent executables from being installed
%global cargo_install_bin 0

%global crate protox

Name:           rust-protox
Version:        0.8.0
Release:        %autorelease
Summary:        Rust implementation of the protobuf compiler

License:        (MIT OR Apache-2.0) AND BSD-3-Clause
URL:            https://crates.io/crates/protox
Source:         %{crates_source}
# Manually created patch for downstream crate metadata changes
# * Fix the license metadata
#   https://github.com/andrewhickman/protox/pull/92
Patch:          protox-fix-metadata.diff

BuildRequires:  cargo-rpm-macros >= 26

%global _description %{expand:
A rust implementation of the protobuf compiler.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch

Provides:       bundled(protobuf) = 3.21.3

%description    devel %{_description}

This package contains library source intended for building other packages which
use the "%{crate}" crate.

%files          devel
%license %{crate_instdir}/LICENSE-APACHE
%license %{crate_instdir}/LICENSE-MIT
%license %{crate_instdir}/protobuf/LICENSE
%doc %{crate_instdir}/README.md
%{crate_instdir}/

%package     -n %{name}+default-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+default-devel %{_description}

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%files       -n %{name}+default-devel
%ghost %{crate_instdir}/Cargo.toml

%prep
%autosetup -n %{crate}-%{version} -p1
%cargo_prep
# Broken test because tests.rs is not in crate
sed -i '/#\[cfg(test)\]/,/mod tests/d' src/file/mod.rs
sed -i '/#\[cfg(test)\]/,/mod tests/d' src/compile/mod.rs

%generate_buildrequires
%cargo_generate_buildrequires -f bin

%build
%cargo_build -f bin

%install
%cargo_install -f bin

%if %{with check}
%check
%cargo_test -f bin
%endif

%changelog
%autochangelog
