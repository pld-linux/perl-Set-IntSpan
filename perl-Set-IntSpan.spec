%include	/usr/lib/rpm/macros.perl
Summary:	Set-IntSpan perl module
Summary(pl):	Modu� perla Set-IntSpan
Name:		perl-Set-IntSpan
Version:	1.07
Release:	5
License:	GPL
Group:		Development/Languages/Perl
Group(de):	Entwicklung/Sprachen/Perl
Group(pl):	Programowanie/J�zyki/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Set/Set-IntSpan-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Set-IntSpan perl module.

%description -l pl
Modu� perla Set-IntSpan.

%prep
%setup -q -n Set-IntSpan-%{version}

%build
perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf Changes README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%{perl_sitelib}/Set/IntSpan.pm
%{_mandir}/man3/*
