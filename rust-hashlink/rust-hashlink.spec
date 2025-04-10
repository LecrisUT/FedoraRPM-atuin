# Generated by rust2rpm 27
%bcond check 1
%global debug_package %{nil}

%global crate hashlink

Name:           rust-hashlink
Version:        0.10.0
Release:        %autorelease
Summary:        HashMap-like containers that hold their key-value pairs in a user controllable order

License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/hashlink
Source:         %{crates_source}

BuildRequires:  cargo-rpm-macros >= 24

%global _description %{expand:
HashMap-like containers that hold their key-value pairs in a user
controllable order.}

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

%package     -n %{name}+serde-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+serde-devel %{_description}

This package contains library source intended for building other packages which
use the "serde" feature of the "%{crate}" crate.

%files       -n %{name}+serde-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+serde_impl-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+serde_impl-devel %{_description}

This package contains library source intended for building other packages which
use the "serde_impl" feature of the "%{crate}" crate.

%files       -n %{name}+serde_impl-devel
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
