%define module  Perl6-Junction
%define name    perl-%{module}
%define version 1.30000
%define release %mkrel 4

Name:           %{name}
Version:        %{version}
Release:        %{release}
Summary:        Perl6 style Junction operators in Perl5
License:        Artistic/GPL
Group:          Development/Perl
URL:            http://search.cpan.org/dist/%{module}
Source:         http://www.cpan.org/modules/by-module/Data/%{module}-%{version}.tar.gz
BuildArch:      noarch
Buildroot:      %{_tmppath}/%{name}-%{version}

%description
This is a lightweight module which provides 'Junction' operators, the most
commonly used being any and all.

Inspired by the Perl6 design docs,
http://dev.perl.org/perl6/doc/design/exe/E06.html.

%prep
%setup -q -n %{module}-%{version}

%build
%{__perl} Makefile.PL installdirs=vendor
%make

%check
%make test

%install
%{__rm} -rf %{buildroot}
%makeinstall_std

%files
%defattr(-,root,root)
%doc README Changes
%{perl_vendorlib}/*
%{_mandir}/*/*

%clean
rm -rf %{buildroot}
