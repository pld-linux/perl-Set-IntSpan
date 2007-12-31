#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Set
%define		pnam	IntSpan
Summary:	Set::IntSpan Perl module - manages sets of integers
Summary(pl.UTF-8):	Moduł Perla Set::IntSpan - zarządzanie zbiorami liczb całkowitych
Name:		perl-Set-IntSpan
Version:	1.13
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	c1633328e9bfece889abe0949992ce04
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Set::IntSpan manages sets of integers. It is optimized for sets that
have long runs of consecutive integers. These arise, for example, in
.newsrc files, which maintain lists of articles.

%description -l pl.UTF-8
Moduł Set::IntSpan zarządza zbiorami liczb całkowitych. Jest
zoptymalizowany dla zbiorów, które mają długie ciągi kolejnych liczb.
Jest to częste na przykład w plikach .newsrc, które zawierają listy
artykułów.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

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
%doc Changes README
%{perl_vendorlib}/Set/IntSpan.pm
%{_mandir}/man3/*
