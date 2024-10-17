%define	version	0.101
%define	name	karpski
%define release %mkrel 17

Summary:	A free ethernet protocol analyzer / sniffer
Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	GPL
Group:		Monitoring
Source:		%{name}-%{version}.tar.bz2
Patch0:		karpski.patch.bz2
Patch1:		karpski-bob.patch.bz2
Patch2:		karpski-green.patch.bz2
URL:		https://mojo.calyx.net/~btx/karpski.html
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:  libpcap-devel
BuildRequires:  gtk-devel

%description
K.ARP.SKI (karpski) is an ethernet protocol analyzer / sniffer.  Its
abilities as a sniffer or scanner are limited, but this sniffer is much
easier to use than other popular sniffers such as tcpdump.  In addition,
there is a protocol definition file in which other protocols can be added. 
Karpski may also be used to launch programs against addresses on your local
network and as a local network intrusion tool.  Plus, it's free with source.

Its display is an Xwindow display.  This was a design decision based on my
need to display many windows simultaneously.  Console mode would just not
cut it.  I chose the Gtk display library because it's proven, portable and
free.  You may not like my choice; the source is included.

This program was originally based on my desire to detect someone plugging an
unauthorized computer into a LAN.  It did this originally by looking at ARP
packets.  This is where the arp in karpski comes from.

%prep
rm -rf $RPM_BUILD_ROOT

%setup 
%patch0 -p1
%patch1 -p1
%patch2 -p1
./configure --prefix=$RPM_BUILD_ROOT%{_prefix} --exec_prefix=/usr/X11R6/bin --datadir=%{_datadir} --libdir=%_libdir
	
%build
%make

%install
make	install-strip prefix="$RPM_BUILD_ROOT%{_prefix}" \
	exec_prefix="$RPM_BUILD_ROOT/usr/X11R6/bin" \
	datfilesdir="$RPM_BUILD_ROOT%{_datadir}/karpski/datfiles" \
	pixmapsdir="$RPM_BUILD_ROOT%{_datadir}/karpski/pixmaps" \
	mandir="$RPM_BUILD_ROOT%{_mandir}"

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr (-,root,root)
%{_datadir}/karpski/datfiles/*
%{_datadir}/karpski/pixmaps/*
%{_mandir}/man8/*
%{_sbindir}/*
%dir %{_datadir}/karpski
%dir %{_datadir}/karpski/datfiles
%dir %{_datadir}/karpski/pixmaps 



%changelog
* Fri Dec 10 2010 Oden Eriksson <oeriksson@mandriva.com> 0.101-17mdv2011.0
+ Revision: 619878
- the mass rebuild of 2010.0 packages

* Fri Sep 11 2009 Thierry Vignaud <tv@mandriva.org> 0.101-16mdv2010.0
+ Revision: 438069
- rebuild

* Wed Oct 29 2008 Oden Eriksson <oeriksson@mandriva.com> 0.101-15mdv2009.1
+ Revision: 298266
- rebuilt against libpcap-1.0.0

* Fri Jul 25 2008 Thierry Vignaud <tv@mandriva.org> 0.101-14mdv2009.0
+ Revision: 247503
- rebuild

* Wed Jan 02 2008 Olivier Blin <oblin@mandriva.com> 0.101-12mdv2008.1
+ Revision: 140850
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request
    - import karpski


* Fri Dec 23 2005 Nicolas Lécureuil <neoclust@mandriva.org> 0.101-12mdk
- Fix BuildRequires
- use mkrel

* Wed Jul 13 2005 Oden Eriksson <oeriksson@mandriva.com> 0.101-11mdk
- rebuilt against new libpcap-0.9.1 (aka. a "play safe" rebuild)

* Tue Apr 26 2005 Lenny Cartier <lenny@mandriva.com> 0.101-10mdk
- rebuild

* Mon Feb 23 2004 Lenny Cartier <lenny@mandrakesoft.com> 0.101-9mdk
- rebuild

* Tue Jan 28 2003 Lenny Cartier <lenny@mandrakesoft.com> 0.101-8mdk
- rebuild

* Fri Nov 22 2002 Olivier Thauvin <thauvin@aerov.jussieu.fr> 0.101-7mdk
- BuildRequires libpcap-devel

* Thu Aug 29 2002  Lenny Cartier <lenny@mandrakesoft.com> 0.101-6mdk
- rebuild

* Wed Aug 08 2001 Lenny Cartier <lenny@mandrakesoft.com> 0.101-5mdk
- rebuild

* Fri Jan 12 2001 Lenny Cartier <lenny@mandrakesoft.com> 0.101-4mdk
- rebuild

* Thu Sep 07 2000 Lenny Cartier <lenny@mandrakesoft.com> 0.101-3mdk
- BM
- macros
* Fri Apr 28 2000 Lenny Cartier <lenny@mandrakesoft.com> 0.101-2mdk
- fix group and files section
* Thu Mar 02 2000 Lenny Cartier <lenny@mandrakesoft.com>
- mandrake build
* Thu May 6 1999 David Green <green@couchpotato.net>
- Replaced scroll bars - they had disappeared due to the two functions disappearing as explained below.
* Wed Mar 10 1999 Bert de Bruijn <bob@ccl.kuleuven.ac.be>
- Upgrade to version 0.101
- added patch to remove two lines that contained a function that doesn't
  exist in my gtk version 1.2. It compiles and runs without it, so ...
- modified specfile to use /usr/share/karpski as datadir.
- used "make install-strip" to get a stripped binary (binary rpm size / 4)
* Mon Aug 23 1998 Hugo van der Kooij <hvdkooij@caiw.nl>
- Started making the RPM.
