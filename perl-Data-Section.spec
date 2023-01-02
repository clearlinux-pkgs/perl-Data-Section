#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Data-Section
Version  : 0.200008
Release  : 14
URL      : https://cpan.metacpan.org/authors/id/R/RJ/RJBS/Data-Section-0.200008.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/R/RJ/RJBS/Data-Section-0.200008.tar.gz
Summary  : 'read multiple hunks of data out of your DATA section'
Group    : Development/Tools
License  : Artistic-1.0 Artistic-1.0-Perl GPL-1.0
Requires: perl-Data-Section-license = %{version}-%{release}
Requires: perl-Data-Section-perl = %{version}-%{release}
BuildRequires : buildreq-cpan
BuildRequires : perl(Data::OptList)
BuildRequires : perl(MRO::Compat)
BuildRequires : perl(Params::Util)
BuildRequires : perl(Sub::Exporter)
BuildRequires : perl(Sub::Install)
BuildRequires : perl(Test::FailWarnings)
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
This archive contains the distribution Data-Section,
version 0.200008:
read multiple hunks of data out of your DATA section

%package dev
Summary: dev components for the perl-Data-Section package.
Group: Development
Provides: perl-Data-Section-devel = %{version}-%{release}
Requires: perl-Data-Section = %{version}-%{release}

%description dev
dev components for the perl-Data-Section package.


%package license
Summary: license components for the perl-Data-Section package.
Group: Default

%description license
license components for the perl-Data-Section package.


%package perl
Summary: perl components for the perl-Data-Section package.
Group: Default
Requires: perl-Data-Section = %{version}-%{release}

%description perl
perl components for the perl-Data-Section package.


%prep
%setup -q -n Data-Section-0.200008
cd %{_builddir}/Data-Section-0.200008

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-Data-Section
cp %{_builddir}/Data-Section-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/perl-Data-Section/834a7d9fa28bbe6ad191f6257132a7276f2469d2 || :
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Data::Section.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-Data-Section/834a7d9fa28bbe6ad191f6257132a7276f2469d2

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/*
