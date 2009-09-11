%define	version	0.101
%define	name	karpski
%define release %mkrel 16

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
URL:		http://mojo.calyx.net/~btx/karpski.html
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

