#
# Conditional build:
# _without_tests - do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
Summary:	CDDB perl module
Summary(pl):	Modu³ perla do CDDB
Name:		perl-CDDB_get
Version:	2.23
Release:	1
License:	Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/authors/id/F/FO/FONKIE/CDDB_get-%{version}.tar.gz
# Source0-md5:	6230c08a91ac819fceada544730623be
BuildRequires:	perl-devel >= 5.6
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module/script gets the CDDB info for an audio cd.

%description -l pl
Ten modu³/skrypt zbiera informacje z bazy CDDB dla p³yt audio CD.

%prep
%setup -q -n CDDB_get-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}
%{!?_without_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/cddb.pl
%{perl_vendorlib}/CDDB_get.pm
%{perl_vendorlib}/cddb.pl
%dir %{perl_vendorlib}/auto/CDDB_get
%{perl_vendorlib}/auto/CDDB_get/autosplit.ix
%{_mandir}/man3/*
