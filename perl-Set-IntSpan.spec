%include	/usr/lib/rpm/macros.perl
%define	pdir	Set
%define	pnam	IntSpan
Summary:	Set::IntSpan Perl module - Manages sets of integers
Summary(pl):	Modu³ Perla Set::IntSpan - zarz±dzaj±cy zbiorami liczb ca³kowitych
Name:		perl-Set-IntSpan
Version:	1.07
Release:	10
License:	GPL
Group:		Development/Languages/Perl
Source0:	ftp://ftp.cpan.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	perl >= 5.6
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Set::IntSpan manages sets of integers.  It is optimized for sets that
have long runs of consecutive integers.  These arise, for example, in
.newsrc files, which maintain lists of articles.

%description -l pl
Modu³ Set::IntSpan zarz±dza zbiorami liczb ca³kowitych. Jest
zoptymalizowany dla zbiorów, które maj± d³ugie ci±gi kolejnych liczb.
Jest to czêste na przyk³ad w plikach .newsrc, które zawieraj± listy
artyku³ów.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

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
%doc Changes README
%{perl_sitelib}/Set/IntSpan.pm
%{_mandir}/man3/*
