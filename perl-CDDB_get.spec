%include	/usr/lib/rpm/macros.perl
Summary:	CDDB perl module
Summary(pl):	Modu³ perla do CDDB
Name:		perl-CDDB_get
Version:	1.61
Release:	2
License:	Artistic
Group:		Development/Languages/Perl
Group(de):	Entwicklung/Sprachen/Perl
Group(pl):	Programowanie/Jêzyki/Perl
Source0:	http://armin.emx.at/cddb/CDDB_get-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module/script gets the CDDB info for an audio cd.

%description -l pl
Ten modu³/skrytp zbiera informacje z bazy CDDB dla p³yt audio CD.

%prep
%setup -q -n CDDB_get-%{version}

%build
perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/cddb.pl
%{perl_sitelib}/CDDB_get.pm
%{_mandir}/man3/*
