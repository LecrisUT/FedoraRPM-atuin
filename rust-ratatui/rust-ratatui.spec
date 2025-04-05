# Generated by rust2rpm 27
%bcond check 1
%global debug_package %{nil}

%global crate ratatui

Name:           rust-ratatui
Version:        0.29.0
Release:        %autorelease
Summary:        Library that's all about cooking up terminal user interfaces

License:        MIT
URL:            https://crates.io/crates/ratatui
Source:         %{crates_source}

BuildRequires:  cargo-rpm-macros >= 24
BuildRequires:  tomcli

%global _description %{expand:
A library that's all about cooking up terminal user interfaces.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages which
use the "%{crate}" crate.

%files          devel
%license %{crate_instdir}/LICENSE
%doc %{crate_instdir}/BREAKING-CHANGES.md
%doc %{crate_instdir}/CHANGELOG.md
%doc %{crate_instdir}/CODE_OF_CONDUCT.md
%doc %{crate_instdir}/MAINTAINERS.md
%doc %{crate_instdir}/README.md
%doc %{crate_instdir}/RELEASE.md
%doc %{crate_instdir}/SECURITY.md
%{crate_instdir}/

%package     -n %{name}+default-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+default-devel %{_description}

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%files       -n %{name}+default-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+all-widgets-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+all-widgets-devel %{_description}

This package contains library source intended for building other packages which
use the "all-widgets" feature of the "%{crate}" crate.

%files       -n %{name}+all-widgets-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+crossterm-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+crossterm-devel %{_description}

This package contains library source intended for building other packages which
use the "crossterm" feature of the "%{crate}" crate.

%files       -n %{name}+crossterm-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+document-features-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+document-features-devel %{_description}

This package contains library source intended for building other packages which
use the "document-features" feature of the "%{crate}" crate.

%files       -n %{name}+document-features-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+macros-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+macros-devel %{_description}

This package contains library source intended for building other packages which
use the "macros" feature of the "%{crate}" crate.

%files       -n %{name}+macros-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+palette-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+palette-devel %{_description}

This package contains library source intended for building other packages which
use the "palette" feature of the "%{crate}" crate.

%files       -n %{name}+palette-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+scrolling-regions-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+scrolling-regions-devel %{_description}

This package contains library source intended for building other packages which
use the "scrolling-regions" feature of the "%{crate}" crate.

%files       -n %{name}+scrolling-regions-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+serde-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+serde-devel %{_description}

This package contains library source intended for building other packages which
use the "serde" feature of the "%{crate}" crate.

%files       -n %{name}+serde-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+termion-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+termion-devel %{_description}

This package contains library source intended for building other packages which
use the "termion" feature of the "%{crate}" crate.

%files       -n %{name}+termion-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+underline-color-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+underline-color-devel %{_description}

This package contains library source intended for building other packages which
use the "underline-color" feature of the "%{crate}" crate.

%files       -n %{name}+underline-color-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+unstable-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+unstable-devel %{_description}

This package contains library source intended for building other packages which
use the "unstable" feature of the "%{crate}" crate.

%files       -n %{name}+unstable-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+unstable-backend-writer-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+unstable-backend-writer-devel %{_description}

This package contains library source intended for building other packages which
use the "unstable-backend-writer" feature of the "%{crate}" crate.

%files       -n %{name}+unstable-backend-writer-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+unstable-rendered-line-info-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+unstable-rendered-line-info-devel %{_description}

This package contains library source intended for building other packages which
use the "unstable-rendered-line-info" feature of the "%{crate}" crate.

%files       -n %{name}+unstable-rendered-line-info-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+unstable-widget-ref-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+unstable-widget-ref-devel %{_description}

This package contains library source intended for building other packages which
use the "unstable-widget-ref" feature of the "%{crate}" crate.

%files       -n %{name}+unstable-widget-ref-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+widget-calendar-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+widget-calendar-devel %{_description}

This package contains library source intended for building other packages which
use the "widget-calendar" feature of the "%{crate}" crate.

%files       -n %{name}+widget-calendar-devel
%ghost %{crate_instdir}/Cargo.toml

%prep
%autosetup -n %{crate}-%{version} -p1
%cargo_prep
# Do not depend on criterion; it is needed only for benchmarks.
tomcli set Cargo.toml del dev-dependencies.criterion
# Do not depend on fakeit; it is needed only for benchmarks.
tomcli set Cargo.toml del dev-dependencies.fakeit
# Remove octocrab dependency and example
tomcli set Cargo.toml del dev-dependencies.octocrab
tomcli set Cargo.toml lists delitem --key=name example async

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
