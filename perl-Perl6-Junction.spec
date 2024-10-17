%define module  Perl6-Junction

Name:		perl-%{module}
Version:	1.60000
Release:	1
Summary:	Perl6 style Junction operators in Perl5
License:	Artistic/GPL
Group:		Development/Perl
URL:		https://search.cpan.org/dist/%{module}
Source:		http://www.cpan.org/modules/by-module/Perl6/%{module}-%{version}.tar.gz

BuildRequires:	perl-devel
BuildArch:	noarch

%description
This is a lightweight module which provides 'Junction' operators, the most
commonly used being any and all.

Inspired by the Perl6 design docs,
http://dev.perl.org/perl6/doc/design/exe/E06.html.

%prep
%setup -q -n %{module}-%{version}

%build
perl Makefile.PL installdirs=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc README Changes
%{perl_vendorlib}/*
%{_mandir}/*/*

%changelog
* Mon Apr 25 2011 Funda Wang <fwang@mandriva.org> 1.40000-3mdv2011.0
+ Revision: 658544
- rebuild for updated spec-helper

* Fri Sep 04 2009 Thierry Vignaud <tv@mandriva.org> 1.40000-2mdv2010.0
+ Revision: 430523
- rebuild

* Sun Aug 10 2008 Guillaume Rousse <guillomovitch@mandriva.org> 1.40000-1mdv2009.0
+ Revision: 270509
- new version

* Thu Jul 31 2008 Thierry Vignaud <tv@mandriva.org> 1.30000-5mdv2009.0
+ Revision: 258225
- rebuild

* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 1.30000-4mdv2009.0
+ Revision: 246279
- rebuild

* Fri Dec 21 2007 Olivier Blin <oblin@mandriva.com> 1.30000-2mdv2008.1
+ Revision: 136335
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Mon Aug 06 2007 Olivier Thauvin <nanardon@mandriva.org> 1.30000-2mdv2008.0
+ Revision: 59328
- fix description (thx misc)

* Mon Aug 06 2007 Olivier Thauvin <nanardon@mandriva.org> 1.30000-1mdv2008.0
+ Revision: 59254
- initial release
- Create perl-Perl6-Junction

