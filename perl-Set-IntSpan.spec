%include	/usr/lib/rpm/macros.perl
%define	pdir	Set
%define	pnam	IntSpan
Summary:	Set::IntSpan - Manages sets of integers
Name:		perl-Set-IntSpan
Version:	1.07
Release:	8
License:	GPL
Group:		Development/Languages/Perl
Source0:	ftp://ftp.cpan.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
C<Set::IntSpan> manages sets of integers.  It is optimized for sets
that have long runs of consecutive integers.  These arise, for example,
in .newsrc files, which maintain lists of articles:

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

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
