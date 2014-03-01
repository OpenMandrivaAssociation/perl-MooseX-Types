%define upstream_name    MooseX-Types%define upstream_version 0.41

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    1

Summary:    Organise your Moose types in libraries
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/MooseX/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(Carp)
BuildRequires: perl(namespace::autoclean)
BuildRequires: perl(Carp::Clan)
BuildRequires: perl(Class::MOP)
BuildRequires: perl(FindBin)
BuildRequires: perl(Moose) > 0.60
BuildRequires: perl(Sub::Install)
BuildRequires: perl(Sub::Uplevel)
BuildRequires: perl(Test::More)
BuildRequires: perl(Test::Exception)
BuildRequires: perl(Test::Fatal)
BuildRequires: perl(Test::Requires)
BuildRequires: perl(Data::Dump)
BuildRequires: perl-namespace-clean
BuildRequires: perl-devel
BuildArch: noarch
Requires: perl-namespace-clean

%description
The types provided with the Moose manpage are by design global. This
package helps you to organise and selectively import your own and the
built-in types in libraries. As a nice side effect, it catches typos at
compile-time too.

However, the main reason for this module is to provide an easy way to not
have conflicts with your type names, since the internal fully qualified
names of the types will be prefixed with the library's name.

This module will also provide you with some helper functions to make it
easier to use Moose types in your code.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor --skipdeps
%make

%check
make test

%install
%makeinstall_std

%files
%doc Changes README
%{_mandir}/man3/*
%perl_vendorlib/MooseX


%changelog
* Mon Jun 13 2011 Guillaume Rousse <guillomovitch@mandriva.org> 0.270.0-1mdv2011.0
+ Revision: 684777
- update to new version 0.27

* Mon Dec 06 2010 Guillaume Rousse <guillomovitch@mandriva.org> 0.250.0-1mdv2011.0
+ Revision: 612306
- update to new version 0.25

* Tue Oct 19 2010 Guillaume Rousse <guillomovitch@mandriva.org> 0.240.0-1mdv2011.0
+ Revision: 586771
- new version

* Sun Jul 25 2010 Guillaume Rousse <guillomovitch@mandriva.org> 0.230.0-1mdv2011.0
+ Revision: 558815
- new version

* Tue Jul 13 2010 Jérôme Quelin <jquelin@mandriva.org> 0.220.0-1mdv2011.0
+ Revision: 552424
- update to 0.22

* Thu Dec 24 2009 Jérôme Quelin <jquelin@mandriva.org> 0.210.0-1mdv2010.1
+ Revision: 482077
- update to 0.21

* Sun Sep 13 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.200.0-1mdv2010.0
+ Revision: 438654
- update to new version 0.20

* Tue Aug 25 2009 Jérôme Quelin <jquelin@mandriva.org> 0.190.0-1mdv2010.0
+ Revision: 421130
- update to 0.19

* Wed Aug 19 2009 Jérôme Quelin <jquelin@mandriva.org> 0.170.0-1mdv2010.0
+ Revision: 418124
- update to 0.17

* Wed Jul 29 2009 Jérôme Quelin <jquelin@mandriva.org> 0.160.0-1mdv2010.0
+ Revision: 404043
- rebuild using %%perl_convert_version

* Tue Jun 30 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.16-1mdv2010.0
+ Revision: 390839
- update to new version 0.16

* Mon Jun 29 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.15-1mdv2010.0
+ Revision: 390523
- update to new version 0.15

* Sun Jun 28 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.14-1mdv2010.0
+ Revision: 390365
- update to new version 0.14

* Thu Jun 25 2009 Jérôme Quelin <jquelin@mandriva.org> 0.13-1mdv2010.0
+ Revision: 389037
- update to new version 0.13

* Thu Jun 18 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.12-1mdv2010.0
+ Revision: 387014
- update to new version 0.12

* Sun May 24 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.11-1mdv2010.0
+ Revision: 379180
- new version

* Sun Mar 08 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.10-1mdv2009.1
+ Revision: 352915
- update to new version 0.10

* Wed Mar 04 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.09-1mdv2009.1
+ Revision: 348399
- update to new version 0.09

* Sun Feb 22 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.08-2mdv2009.1
+ Revision: 343856
- fix dependencies

* Sun Dec 14 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.08-1mdv2009.1
+ Revision: 314254
- update to new version 0.08

* Sun Nov 09 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.07-1mdv2009.1
+ Revision: 301323
- update to new version 0.07

* Mon Oct 27 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.06-1mdv2009.1
+ Revision: 297782
- new version

* Wed Jul 16 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.04-1mdv2009.0
+ Revision: 236371
- import perl-MooseX-Types


* Wed Jul 16 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.04-1mdv2009.0
- initial mdv release, generated with cpan2dist

