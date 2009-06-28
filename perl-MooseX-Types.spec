%define module   MooseX-Types
%define version    0.14
%define release    %mkrel 1

Name:       perl-%{module}
Version:    %{version}
Release:    %{release}
License:    GPL or Artistic
Group:      Development/Perl
Summary:    Organise your Moose types in libraries
Url:        http://search.cpan.org/dist/%{module}
Source:     http://www.cpan.org/modules/by-module/MooseX/%{module}-%{version}.tar.gz
BuildRequires: perl(Carp)
BuildRequires: perl(Carp::Clan)
BuildRequires: perl(Class::MOP)
BuildRequires: perl(FindBin)
BuildRequires: perl(Moose) > 0.60
BuildRequires: perl(Sub::Install)
BuildRequires: perl(Sub::Uplevel)
BuildRequires: perl(Test::More)
BuildRequires: perl(Test::Exception)
BuildRequires: perl(Data::Dump)
BuildRequires: perl-namespace-clean
Requires: perl-namespace-clean
BuildArch: noarch
BuildRoot:  %{_tmppath}/%{name}-%{version}

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
%setup -q -n %{module}-%{version} 

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor --skipdeps
%make

%check
make test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc Changes README
%{_mandir}/man3/*
%perl_vendorlib/MooseX

