%define name	kmflcomp
%define version	0.9.6
%define release	%mkrel 1

%define major		0
%define libname		%mklibname %name %major
%define develname	%mklibname %name -d

Name:		%{name}
Summary:	Compiler for source Tavultesoft Keyman files
Version:	%{version}
Release:	%{release}
Group:		System/Internationalization
License:	GPLv2+
URL:		http://kmfl.sourceforge.net/
Source0:	http://prdownloads.sourceforge.net/kmfl/%{name}-%{version}.tar.gz
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	bison
BuildRequires:	libx11-devel
BuildRequires:	libxau-devel
BuildRequires:	libxdmcp-devel

%description
KMFL is a keyboarding input method which aims to bring Tavultesoft
Keyman functionality to Linux.

kmflcomp is one of three parts of the KMFL project. It is a keyboard
compiler. The other two parts are libkmfl and libscim-kmfl-imengine.

%package -n %libname
Summary:	Kmflcomp library
Group:		System/Internationalization

%description -n %libname
KMFL is a keyboarding input method which aims to bring Tavultesoft
Keyman functionality to Linux.

libkmflcomp is one of three parts of the KMFL project. It is a 
keyboard compiler library. The other two parts are libkmfl and 
libscim-kmfl-imengine.


%package -n %{develname}
Summary:	Kmflcomp library
Group:		Development/C
Requires:	%libname = %version
Provides:	lib%{name}-devel
Obsoletes:	%{mklibname kmflcomp 0 -d}


%description -n %{develname}
Headers and static library of Kmflcomp.


%prep
%setup -q

%build
%configure2_5x
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

# remove documents (AUTHORS, COPYING etc.)
# they should be installed by %doc
rm -rf %{buildroot}/%{_prefix}/doc/

%clean
rm -rf $RPM_BUILD_ROOT

%post -n %libname -p /sbin/ldconfig
%postun -n %libname -p /sbin/ldconfig

%files
%defattr(-,root,root)
%doc AUTHORS ChangeLog
%{_bindir}/kmflcomp

%files -n %libname
%defattr(-,root,root)
%_libdir/libkmflcomp.so.*

%files -n %{develname}
%defattr(-,root,root)
%_includedir/kmfl
%_libdir/libkmflcomp.a
%_libdir/libkmflcomp.la
%_libdir/libkmflcomp.so
