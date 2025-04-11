# Generated by rust2rpm 27
%bcond check 1
%global debug_package %{nil}

%global crate prost-reflect

Name:           rust-prost-reflect
Version:        0.15.0
Release:        %autorelease
Summary:        Protobuf library extending prost with reflection support and dynamic messages

License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/prost-reflect
Source:         %{crates_source}

BuildRequires:  cargo-rpm-macros >= 24
BuildRequires:  tomcli

%global _description %{expand:
A protobuf library extending prost with reflection support and dynamic
messages.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages which
use the "%{crate}" crate.

%files          devel
%license %{crate_instdir}/LICENSE-APACHE
%license %{crate_instdir}/LICENSE-MIT
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

%package     -n %{name}+miette-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+miette-devel %{_description}

This package contains library source intended for building other packages which
use the "miette" feature of the "%{crate}" crate.

%files       -n %{name}+miette-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+serde-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+serde-devel %{_description}

This package contains library source intended for building other packages which
use the "serde" feature of the "%{crate}" crate.

%files       -n %{name}+serde-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+text-format-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+text-format-devel %{_description}

This package contains library source intended for building other packages which
use the "text-format" feature of the "%{crate}" crate.

%files       -n %{name}+text-format-devel
%ghost %{crate_instdir}/Cargo.toml

%prep
%autosetup -n %{crate}-%{version} -p1
%cargo_prep
# Relax logos dependency
tomcli set Cargo.toml str dependencies.logos.version '>=0.14.0,<0.16'
# Broken test because tests.rs is not in crate
sed -i '/#\[cfg(test)\]/,/mod tests/d' src/descriptor/mod.rs

%generate_buildrequires
%cargo_generate_buildrequires

%build
%cargo_build

%install
%cargo_install

%if %{with check}
%check
# * - Almost all tests are skipped because they require file_descriptor_set.bin
#   which is not included.
# * - dynamic::type_sizes This test uses std::mem::size_of which is inconsistent
#   on i686
%{cargo_test -- -- %{shrink:
    --skip dynamic::DynamicMessage::decode
    --skip dynamic::DynamicMessage::fmt
    --skip dynamic::DynamicMessage::has_field
    --skip dynamic::DynamicMessage::try_set_field
    --skip dynamic::DynamicMessage::try_set_field_by_name
    --skip dynamic::DynamicMessage::try_set_field_by_number
    --skip dynamic::unknown::UnknownField::decode
    --skip dynamic::unknown::UnknownField::decode_value
    --skip dynamic::unknown::UnknownField::fmt
    --skip src/lib.rs
    --skip dynamic::type_sizes
}}
%endif

%changelog
%autochangelog
