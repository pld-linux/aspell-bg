Summary:	Bulgarian dictionary for aspell
Summary(bg):	��������� ������ �� �������� �� ��������� �� GNU Aspell
Summary(pl):	Bu�garski s�ownik dla aspella
Name:		aspell-bg
Version:	4.0
%define	subv	0
Release:	1
License:	GPL
Group:		Applications/Text
Source0:	ftp://ftp.gnu.org/gnu/aspell/dict/bg/aspell5-bg-%{version}-%{subv}.tar.bz2
# Source0-md5:	f1d9f1587cc382f10f1c7ac0a2600833
URL:		http://aspell.net/
BuildRequires:	aspell >= 0.50.0
Requires:	aspell >= 0.50.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Bulgarian dictionary (i.e. word list) for aspell.

%description -l bg
��������� ������ �� �������� �� ��������� �� GNU Aspell.

%description -l pl
Bu�garski s�ownik (lista s��w) dla aspella.

%prep
%setup -q -n aspell5-bg-%{version}-%{subv}

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
%{_libdir}/aspell/*
%{_datadir}/aspell/*
