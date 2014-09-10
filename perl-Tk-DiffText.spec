#
# Conditional build:
%bcond_without	tests		# do not perform "make test"

%define		pdir	Tk
%define		pnam	DiffText
%include	/usr/lib/rpm/macros.perl
Summary:	Tk::DiffText - Perl/Tk composite widget for colorized diffs
Name:		perl-Tk-DiffText
Version:	0.19
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Tk/%{pdir}-%{pnam}-%{version}.zip
# Source0-md5:	02a06caf724c6f25ed6b138affcb14d7
URL:		http://search.cpan.org/dist/Tk-DiffText/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-Algorithm-Diff >= 1.13
BuildRequires:	perl-Tie-Tk-Text >= 0.01
BuildRequires:	perl-Tk
%endif
Requires:	perl-Algorithm-Diff >= 1.13
Requires:	perl-Tie-Tk-Text >= 0.01
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module defines a composite widget that makes it simple to provide
basic "diff" functionality to your Tk applications.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{_mandir}/man3/Tk::DiffText.3pm*
%{perl_vendorlib}/Tk/DiffText.pm
