#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Pod
%define		pnam	ToDemo
Summary:	Pod::ToDemo - writes a demo program from a tutorial POD
Summary(pl):	Pod::ToDemo - tworzenie demonstracyjnego programu z tutorialu POD
Name:		perl-Pod-ToDemo
Version:	0.21
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	6a93ec17627bce5baff709606276dc55
URL:		http://search.cpan.org/dist/Pod-ToDemo/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	perl-Module-Build
%if %{with tests}
BuildRequires:	perl(Test::Exception)
BuildRequires:	perl(Test::Simple) >= 0.47
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

%description -l pl
Pod::ToDemo pozwala na pisanie modu³ów POD s³u¿±cych jako tutoriale,
potrafi±ce wypisaæ demonstracyjne programy, je¶li zostan± wywo³ane
bezpo¶rednio. To znaczy, je¶li SDL::Tutorial jest tutorialem
dotycz±cym pisania podstawowych aplikacji korzystaj±cych z SDL w
Perlu, mo¿liwe jest wywo³anie go jako:

	$ perl -MSDL::Tutorial sdl_demo.pl

w wyniku czego otrzymamy plik sdl_demo.pl bêd±cy demonstracyjnym
programem stworzonym na podstawie tutoriala.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Build.PL \
	installdirs=vendor \
	destdir=$RPM_BUILD_ROOT
./Build

%{?with_tests:./Build test}

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT{%{perl_vendorlib}/Pod,%{_mandir}/man3}

./Build install 

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/Pod/*.pm
%{_mandir}/man3/*
