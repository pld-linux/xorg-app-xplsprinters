# $Rev: 3411 $, $Date: 2005-08-27 17:42:47 $
#
Summary:	xplsprinters application
Summary(pl):	Aplikacja xplsprinters
Name:		xorg-app-xplsprinters
Version:	0.99.0
Release:	0.02
License:	MIT
Group:		X11/Applications
Source0:	http://xorg.freedesktop.org/X11R7.0-RC0/app/xplsprinters-%{version}.tar.bz2
# Source0-md5:	1783c4c426673c82f57cdb39f7c9c108
Patch0:		xplsprinters-man.patch
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	xorg-lib-libXprintUtil-devel
BuildRequires:	xorg-util-util-macros
BuildRequires:	pkgconfig >= 0.19
BuildRoot:	%{tmpdir}/xplsprinters-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

%description
xplsprinters application.

%description -l pl
Aplikacja xplsprinters.


%prep
%setup -q -n xplsprinters-%{version}
%patch0 -p1


%build
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure

%{__make}


%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(644,root,root,755)
%attr(755,root,wheel) %{_bindir}/*
%{_mandir}/man1/*.1*
