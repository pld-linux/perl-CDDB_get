#
# Conditional build:
%bcond_without	tests # do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	CDDB_get
Summary:	CDDB - read the CDDB entry for an audio CD in your drive
Summary(pl.UTF-8):	CDDB - odczyt informacji CDDB dla płyty audio CD w napędzie
Name:		perl-CDDB_get
Version:	2.27
Release:	2
License:	GPL v2 or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-authors/id/F/FO/FONKIE/%{pdir}-%{version}.tar.gz
# Source0-md5:	405a3704ad5db45f117cc7cc5bd1ce7c
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module/script gets the CDDB info for an audio cd.

%description -l pl.UTF-8
Ten moduł/skrypt zbiera informacje z bazy CDDB dla płyt audio CD.

%prep
%setup -q -n %{pdir}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/cddb.pl
%{perl_vendorlib}/CDDB_cache.pm
%{perl_vendorlib}/CDDB_get.pm
%{perl_vendorlib}/cddb.pl
%dir %{perl_vendorlib}/auto/CDDB_cache
%{perl_vendorlib}/auto/CDDB_cache/autosplit.ix
%dir %{perl_vendorlib}/auto/CDDB_get
%{perl_vendorlib}/auto/CDDB_get/autosplit.ix
%{_mandir}/man3/*
