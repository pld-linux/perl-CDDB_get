#
# Conditional build:
# _without_tests - do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
Summary:	CDDB perl module
Summary(pl):	Modu� perla do CDDB
Name:		perl-CDDB_get
Version:	2.11
Release:	2
License:	Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/authors/id/F/FO/FONKIE/CDDB_get-%{version}.tar.gz
BuildRequires:	perl >= 5.6
BuildRequires:	rpm-perlprov >= 4.0.2-104
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module/script gets the CDDB info for an audio cd.

%description -l pl
Ten modu�/skrypt zbiera informacje z bazy CDDB dla p�yt audio CD.

%prep
%setup -q -n CDDB_get-%{version}

%build
%{__perl} Makefile.PL
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
%{perl_sitelib}/CDDB_get.pm
%{perl_sitelib}/cddb.pl
%dir %{perl_sitelib}/auto/CDDB_get
%{perl_sitelib}/auto/CDDB_get/autosplit.ix
%{_mandir}/man3/*
