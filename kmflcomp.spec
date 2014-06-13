%define major	0
%define libname	%mklibname %name %major
%define devname	%mklibname %name -d

Summary:	Compiler for source Tavultesoft Keyman files
Name:		kmflcomp
Version:	0.9.9
Release:	7
Group:		System/Internationalization
License:	GPLv2+
Url:		http://kmfl.sourceforge.net/
Source0:	http://prdownloads.sourceforge.net/kmfl/%{name}-%{version}.tar.gz
Patch0:		kmflcomp-0.9.8-linkage.patch

BuildRequires:	bison
BuildRequires:	pkgconfig(x11)
BuildRequires:	pkgconfig(xau)
BuildRequires:	pkgconfig(xdmcp)

%description
KMFL is a keyboarding input method which aims to bring Tavultesoft
Keyman functionality to Linux.

kmflcomp is one of three parts of the KMFL project. It is a keyboard
compiler. The other two parts are libkmfl and libscim-kmfl-imengine.

%package -n %{libname}
Summary:	Kmflcomp library
Group:		System/Internationalization

%description -n %{libname}
KMFL is a keyboarding input method which aims to bring Tavultesoft
Keyman functionality to Linux.

libkmflcomp is one of three parts of the KMFL project. It is a 
keyboard compiler library. The other two parts are libkmfl and 
libscim-kmfl-imengine.

%package -n %{devname}
Summary:	Kmflcomp library
Group:		Development/C
Requires:	%{libname} = %{version}
Provides:	%{name}-devel = %{version}-%{release}

%description -n %{devname}
Headers and static library of Kmflcomp.

%prep
%setup -q
%apply_patches

%build
%configure2_5x

%make

%install
%makeinstall_std

# remove documents (AUTHORS, COPYING etc.)
# they should be installed by %doc
rm -rf %{buildroot}/%{_prefix}/doc/

%files
%doc AUTHORS ChangeLog
%{_bindir}/kmflcomp

%files -n %{libname}
%{_libdir}/libkmflcomp.so.%{major}*

%files -n %{devname}
%{_includedir}/kmfl
%{_libdir}/libkmflcomp.a
%{_libdir}/libkmflcomp.so

