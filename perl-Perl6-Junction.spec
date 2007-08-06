%define module  Perl6-Junction
%define name    perl-%{module}
%define version 1.30000
%define release %mkrel 1

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
Data::FormValidator's main aim is to make input validation expressible in a
simple format. Data::FormValidator lets you define profiles which declare the
required and optional fields and any constraints they might have.

The results are provided as an object which makes it easy to handle missing and
invalid results, return error messages about which constraints failed, or
process the resulting valid data.

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

