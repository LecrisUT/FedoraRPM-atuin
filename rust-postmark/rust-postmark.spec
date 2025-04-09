# Generated by rust2rpm 27
%bcond check 1
%global debug_package %{nil}

%global crate postmark

Name:           rust-postmark
Version:        0.11.2
Release:        %autorelease
Summary:        Rust client

# Upstream license specification: MIT/Apache-2.0
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/postmark
Source:         %{crates_source}

BuildRequires:  cargo-rpm-macros >= 24

%global _description %{expand:
Postmark rust client.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages which
use the "%{crate}" crate.

%files          devel
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

%package     -n %{name}+indexmap-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+indexmap-devel %{_description}

This package contains library source intended for building other packages which
use the "indexmap" feature of the "%{crate}" crate.

%files       -n %{name}+indexmap-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+reqwest-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+reqwest-devel %{_description}

This package contains library source intended for building other packages which
use the "reqwest" feature of the "%{crate}" crate.

%files       -n %{name}+reqwest-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+reqwest-native-tls-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+reqwest-native-tls-devel %{_description}

This package contains library source intended for building other packages which
use the "reqwest-native-tls" feature of the "%{crate}" crate.

%files       -n %{name}+reqwest-native-tls-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+reqwest-rustls-tls-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+reqwest-rustls-tls-devel %{_description}

This package contains library source intended for building other packages which
use the "reqwest-rustls-tls" feature of the "%{crate}" crate.

%files       -n %{name}+reqwest-rustls-tls-devel
%ghost %{crate_instdir}/Cargo.toml

%prep
%autosetup -n %{crate}-%{version} -p1
%cargo_prep

%generate_buildrequires
%cargo_generate_buildrequires -a

%build
%cargo_build -a

%install
%cargo_install -a

%if %{with check}
%check
%cargo_test -a
%endif

%changelog
%autochangelog
