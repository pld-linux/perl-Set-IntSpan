%include	/usr/lib/rpm/macros.perl
%define	pdir	Set
%define	pnam	IntSpan
Summary:	Set::IntSpan Perl module - Manages sets of integers
Summary(pl):	Modu� Perla Set::IntSpan - zarz�dzaj�cy zbiorami liczb ca�kowitych
Name:		perl-Set-IntSpan
Version:	1.07
Release:	11
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	2f8839d5897f1f0597bff1e6475004bb
BuildRequires:	perl-devel >= 5.6
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Set::IntSpan manages sets of integers.  It is optimized for sets that
have long runs of consecutive integers.  These arise, for example, in
.newsrc files, which maintain lists of articles.

%description -l pl
Modu� Set::IntSpan zarz�dza zbiorami liczb ca�kowitych. Jest
zoptymalizowany dla zbior�w, kt�re maj� d�ugie ci�gi kolejnych liczb.
Jest to cz�ste na przyk�ad w plikach .newsrc, kt�re zawieraj� listy
artyku��w.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor 
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/Set/IntSpan.pm
%{_mandir}/man3/*
