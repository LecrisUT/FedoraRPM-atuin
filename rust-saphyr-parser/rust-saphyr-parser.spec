# Generated by rust2rpm 27
%bcond check 1
%global debug_package %{nil}

# prevent executables from being installed
%global cargo_install_bin 0

%global crate saphyr-parser

Name:           rust-saphyr-parser
Version:        0.0.3
Release:        %autorelease
Summary:        Fully YAML 1.2 compliant YAML library

License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/saphyr-parser
Source:         %{crates_source}

BuildRequires:  cargo-rpm-macros >= 26

%global _description %{expand:
A fully YAML 1.2 compliant YAML library.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages which
use the "%{crate}" crate.

%files          devel
%license %{crate_instdir}/.licenses/ChenYuheng-Apache
%license %{crate_instdir}/.licenses/ChenYuheng-MIT
%license %{crate_instdir}/.licenses/Ethiraric-Apache
%license %{crate_instdir}/.licenses/Ethiraric-MIT
%license %{crate_instdir}/LICENSE
%doc %{crate_instdir}/CHANGELOG.md
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

%package     -n %{name}+debug_prints-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+debug_prints-devel %{_description}

This package contains library source intended for building other packages which
use the "debug_prints" feature of the "%{crate}" crate.

%files       -n %{name}+debug_prints-devel
%ghost %{crate_instdir}/Cargo.toml

%prep
%autosetup -n %{crate}-%{version} -p1
%cargo_prep

%generate_buildrequires
%cargo_generate_buildrequires

%build
%cargo_build

%install
%cargo_install

%if %{with check}
%check
%cargo_test
%endif

%changelog
%autochangelog
