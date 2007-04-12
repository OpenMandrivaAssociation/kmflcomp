%define version	0.8
%define release	%mkrel 6

%define libname %mklibname %name 0

#%define libkmfl_version	0.5

Name:		kmflcomp
Summary:	Compiler for source Tavultesoft Keyman files
Version:		%{version}
Release:		%{release}
Group:		System/Internationalization
License:		GPL
URL:			http://kmfl.sourceforge.net/
Source0:		%{name}-%{version}.tar.bz2
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
#Requires:			libkmfl >= %{libkmfl_version}
#BuildRequires:		libkmfl-devel >= %{libkmfl_version}
BuildRequires:		automake1.8
BuildRequires:		bison
BuildRequires:		XFree86-devel

%description
Kmflcomp is a compiler for source Tavultesoft Keyman files.
Libkmfl uses the binary Keyman files compiled by kmflcomp.

%package -n %libname
Summary:	Kmflcomp library
Group:		System/Internationalization

%description -n %libname
This is the library of Kmflcomp.


%package -n %{libname}-devel
Summary:	Kmflcomp library
Group:		Development/C
Requires:	%libname = %version
Provides:	lib%{name}-devel
Conflicts:  %mklibname kmfl 0 < 0.8

%description -n %{libname}-devel
Headers and static library of Kmflcomp.


%prep
%setup -q
cp /usr/share/automake-1.9/mkinstalldirs .

%build
[[ ! -x configure ]] && ./autogen.sh
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
%doc COPYING
%{_bindir}/kmflcomp

%files -n %libname
%defattr(-,root,root)
%_libdir/libkmflcomp.so.*

%files -n %{libname}-devel
%defattr(-,root,root)
%_includedir/kmfl
%_libdir/libkmflcomp.a
%_libdir/libkmflcomp.la
%_libdir/libkmflcomp.so


