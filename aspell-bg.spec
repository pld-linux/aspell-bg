Summary:	Bulgarian dictionary for aspell
Summary(bg.UTF-8):	Български речник за проверка на правописа за GNU Aspell
Summary(pl.UTF-8):	Bułgarski słownik dla aspella
Name:		aspell-bg
Version:	4.1
%define	subv	0
Release:	2
License:	GPL v2
Group:		Applications/Text
Source0:	http://ftp.gnu.org/gnu/aspell/dict/bg/aspell6-bg-%{version}-%{subv}.tar.bz2
# Source0-md5:	e22f0634c48eae9c9fbdf9d569b8235c
URL:		http://aspell.net/
BuildRequires:	aspell >= 3:0.60.0
Requires:	aspell >= 3:0.60.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Bulgarian dictionary (i.e. word list) for aspell.

%description -l bg.UTF-8
Български речник за проверка на правописа за GNU Aspell.

%description -l pl.UTF-8
Bułgarski słownik (lista słów) dla aspella.

%prep
%setup -q -n aspell6-bg-%{version}-%{subv}

%build
# note: configure is not autoconf-generated
./configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Copyright README
%lang(bg) %doc doc/README.BULGARIAN
%{_prefix}/lib/aspell/*
%{_datadir}/aspell/*
