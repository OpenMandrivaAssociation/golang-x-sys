# Run tests in check section
%bcond_without check

# https://golang.org/x/sys
%global goipath		golang.org/x/sys
%global forgeurl	https://golang.org/x/sys
Version:		0.25.0

%gometa

Summary:	Supplemental Go packages for low-level interactions with the operating system
Name:		golang-golang.org-x-sys

Release:	1
Source0:	https://github.com/golang/sys/archive/v%{version}/sys-%{version}.tar.gz
URL:		https://golang.org/x/sys
License:	BSD with advertising
Group:		Development/Other
BuildRequires:	compiler(go-compiler)
BuildArch:	noarch

%description
Supplemental Go packages for low-level interactions with the operating system.

#-----------------------------------------------------------------------

%package devel
Summary:	%{summary}
Group:		Development/Other
BuildArch:	noarch

%description devel
%{description}

This package contains library source intended for
building other packages which use import path with
%{goipath} prefix.

%files devel -f devel.file-list
%license LICENSE
%doc README.md

#-----------------------------------------------------------------------

%prep
%autosetup -p1 -n sys-%{version}

%build
%gobuildroot

%install
%goinstall

%check
%if %{with check}
%gochecks
%endif

