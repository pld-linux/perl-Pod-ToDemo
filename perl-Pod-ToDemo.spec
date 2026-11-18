#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%define		pdir	Pod
%define		pnam	ToDemo
Summary:	Pod::ToDemo - writes a demo program from a tutorial POD
Summary(pl.UTF-8):	Pod::ToDemo - tworzenie demonstracyjnego programu z tutorialu POD
Name:		perl-Pod-ToDemo
Version:	1.20110709
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	https://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	f66537cf300da3399b32ddbbfd80168b
URL:		http://search.cpan.org/dist/Pod-ToDemo/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-Test-Exception
BuildRequires:	perl(Test::More)
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Pod::ToDemo allows you to write POD-only modules that serve as
tutorials which can write out demo programs if they're invoked
directly. That is, while SDL::Tutorial is a tutorial on writing
beginner SDL applications with Perl, you can invoke it as:

	$ perl -MSDL::Tutorial sdl_demo.pl

and it will write a bare-bones demo program called sdl_demo.pl, based
on the tutorial.

%description -l pl.UTF-8
Pod::ToDemo pozwala na pisanie modułów POD służących jako tutoriale,
potrafiące wypisać demonstracyjne programy, jeśli zostaną wywołane
bezpośrednio. To znaczy, jeśli SDL::Tutorial jest tutorialem
dotyczącym pisania podstawowych aplikacji korzystających z SDL w
Perlu, możliwe jest wywołanie go jako:

	$ perl -MSDL::Tutorial sdl_demo.pl

w wyniku czego otrzymamy plik sdl_demo.pl będący demonstracyjnym
programem stworzonym na podstawie tutoriala.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/Pod/*.pm
%{_mandir}/man3/*
