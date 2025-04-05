# Generated by rust2rpm 27
%bcond check 1
%global debug_package %{nil}

%global crate divan

Name:           rust-divan
Version:        0.1.18
Release:        %autorelease
Summary:        Statistically-comfy benchmarking library

License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/divan
Source:         %{crates_source}

BuildRequires:  cargo-rpm-macros >= 24

%global _description %{expand:
Statistically-comfy benchmarking library.}

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
%doc %{crate_instdir}/WANTED.md
%{crate_instdir}/

%package     -n %{name}+default-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+default-devel %{_description}

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%files       -n %{name}+default-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+dyn_thread_local-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+dyn_thread_local-devel %{_description}

This package contains library source intended for building other packages which
use the "dyn_thread_local" feature of the "%{crate}" crate.

%files       -n %{name}+dyn_thread_local-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+help-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+help-devel %{_description}

This package contains library source intended for building other packages which
use the "help" feature of the "%{crate}" crate.

%files       -n %{name}+help-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+internal_benches-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+internal_benches-devel %{_description}

This package contains library source intended for building other packages which
use the "internal_benches" feature of the "%{crate}" crate.

%files       -n %{name}+internal_benches-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+wrap_help-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+wrap_help-devel %{_description}

This package contains library source intended for building other packages which
use the "wrap_help" feature of the "%{crate}" crate.

%files       -n %{name}+wrap_help-devel
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
