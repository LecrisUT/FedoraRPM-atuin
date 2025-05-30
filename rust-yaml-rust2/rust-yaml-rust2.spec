# Generated by rust2rpm 27
%bcond check 1
%global debug_package %{nil}

# prevent executables from being installed
%global cargo_install_bin 0

%global crate yaml-rust2

Name:           rust-yaml-rust2
Version:        0.10.2
Release:        %autorelease
Summary:        Fully YAML 1.2 compliant YAML parser

License:        MIT OR (MIT AND Apache-2.0)
URL:            https://crates.io/crates/yaml-rust2
Source:         %{crates_source}
# Manually created patch for downstream crate metadata changes
# * Drop libtest-mimic because it is too old
#   (Used in tests/yaml-test-suite.rs)
# * Relax hashlink dependency to include 0.9
Patch:          yaml-rust2-fix-metadata.diff

BuildRequires:  cargo-rpm-macros >= 26

%global _description %{expand:
A fully YAML 1.2 compliant YAML parser.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages which
use the "%{crate}" crate.

%files          devel
%license %{crate_instdir}/.licenses/Apache-LICENSE
%license %{crate_instdir}/.licenses/MIT-LICENSE
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

%package     -n %{name}+encoding-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+encoding-devel %{_description}

This package contains library source intended for building other packages which
use the "encoding" feature of the "%{crate}" crate.

%files       -n %{name}+encoding-devel
%ghost %{crate_instdir}/Cargo.toml

%prep
%autosetup -n %{crate}-%{version} -p1
%cargo_prep

%generate_buildrequires
%cargo_generate_buildrequires

%build
%cargo_build

%install
# Remove extraneous files from being installed
rm -rf tests/yaml-test-suite documents appveyor.yml garden.yml justfile
%cargo_install
install -Dp .licenses/* -t %{buildroot}%{crate_instdir}/.licenses

%if %{with check}
%check
%cargo_test
%endif

%changelog
%autochangelog
