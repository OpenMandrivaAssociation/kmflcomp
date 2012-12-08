%define major		0
%define libname		%mklibname %name %major
%define develname	%mklibname %name -d

Name:		kmflcomp
Summary:	Compiler for source Tavultesoft Keyman files
Version:	0.9.9
Release:	1
Group:		System/Internationalization
License:	GPLv2+
URL:		http://kmfl.sourceforge.net/
Source0:	http://prdownloads.sourceforge.net/kmfl/%{name}-%{version}.tar.gz
Patch0:		kmflcomp-0.9.8-linkage.patch
BuildRequires:	bison
BuildRequires:	libx11-devel
BuildRequires:	libxau-devel
BuildRequires:	libxdmcp-devel

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

%package -n %{develname}
Summary:	Kmflcomp library
Group:		Development/C
Requires:	%{libname} = %{version}
Provides:	%{name}-devel = %{version}-%{release}
Obsoletes:	%{mklibname kmflcomp 0 -d}

%description -n %{develname}
Headers and static library of Kmflcomp.

%prep
%setup -q
%patch0 -p0

%build
%configure2_5x
%make

%install
%makeinstall_std

# remove documents (AUTHORS, COPYING etc.)
# they should be installed by %doc
rm -rf %{buildroot}/%{_prefix}/doc/

%files
%defattr(-,root,root)
%doc AUTHORS ChangeLog
%{_bindir}/kmflcomp

%files -n %{libname}
%defattr(-,root,root)
%{_libdir}/libkmflcomp.so.%{major}*

%files -n %{develname}
%defattr(-,root,root)
%{_includedir}/kmfl
%{_libdir}/libkmflcomp.a
%{_libdir}/libkmflcomp.so


%changelog
* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 0.9.8-4mdv2011.0
+ Revision: 666030
- mass rebuild

* Fri Dec 03 2010 Oden Eriksson <oeriksson@mandriva.com> 0.9.8-3mdv2011.0
+ Revision: 606266
- rebuild

* Sun Nov 15 2009 Funda Wang <fwang@mandriva.org> 0.9.8-2mdv2010.1
+ Revision: 466184
- fix linkage

* Sun Nov 15 2009 Funda Wang <fwang@mandriva.org> 0.9.8-1mdv2010.1
+ Revision: 466183
- new version 0.9.8

* Wed Sep 02 2009 Christophe Fergeau <cfergeau@mandriva.com> 0.9.7-2mdv2010.0
+ Revision: 425487
- rebuild

* Wed Dec 17 2008 Adam Williamson <awilliamson@mandriva.org> 0.9.7-1mdv2009.1
+ Revision: 315029
- new release 0.9.7
- small cleanups

* Sun Nov 09 2008 Oden Eriksson <oeriksson@mandriva.com> 0.9.6-5mdv2009.1
+ Revision: 301471
- rebuilt against new libxcb

* Sat Jun 28 2008 Oden Eriksson <oeriksson@mandriva.com> 0.9.6-4mdv2009.0
+ Revision: 229909
- fix linkage

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

* Sun Jan 13 2008 Thierry Vignaud <tv@mandriva.org> 0.9.6-2mdv2008.1
+ Revision: 150427
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Thu Sep 06 2007 Adam Williamson <awilliamson@mandriva.org> 0.9.6-1mdv2008.0
+ Revision: 80747
- correct license to GPLv2+
- new release 0.9.6

* Fri Aug 03 2007 Adam Williamson <awilliamson@mandriva.org> 0.9.5-1mdv2008.0
+ Revision: 58432
- rebuild for 2008
- remove unneeded complexity in build
- improve description
- new devel policy
- clean buildrequires
- use Fedora license policy
- spec clean
- new release 0.9.5


* Fri Feb 23 2007 Thierry Vignaud <tvignaud@mandriva.com> 0.8-6mdv2007.0
+ Revision: 125044
- Import kmflcomp

* Fri Feb 23 2007 Thierry Vignaud <tvignaud@mandrakesoft.com> 0.8-6mdv2007.1
- fix group (#28149)

* Fri Jan 20 2006 Christiaan Welvaart <cjw@daneel.dyndns.org> 0.8-5mdk
- drop BuildRequires: fpc (not needed)

* Sat Aug 20 2005 Christiaan Welvaart <cjw@daneel.dyndns.org> 0.8-4mdk
- add BuildRequires: bison XFree86-devel

* Thu Aug 11 2005 Nicolas Lécureuil <neoclust@mandriva.org> 0.8-3mdk
- fix BuildRequires

* Tue Aug 09 2005 Thierry Vignaud <tvignaud@mandriva.com> 0.8-2mdk
- add conflict to ease update

* Tue Aug 09 2005 Thierry Vignaud <tvignaud@mandriva.com> 0.8-1mdk
- new release

* Thu May 12 2005 UTUMI Hirosi <utuhiro78@yahoo.co.jp> 0.5-1mdk
- first spec for Mandriva Linux

