%define _disable_ld_no_undefined 1
%define _disable_ld_as_needed 1

%define major 0
%define libname %mklibname seeks %{major}
%define develname %mklibname seeks -d

Name:		seeks
Version:	0.4.1
Release:	2
Summary:	Open decentralized platform for collaborative search
Group:		Networking/WWW
License:	AGPLv3
URL:		https://www.seeks-project.info/
Source0:	http://www.seeks-project.info/site/releases/%{name}-%{version}.tar.gz
Source1:	seeks.init
Source2:	config.mdv
Patch1:		seeks-0.4.0-mdv-opencv.patch
Requires(pre,post,preun,postun):	rpm-helper
BuildRequires:	pcre-devel
BuildRequires:	curl-devel
BuildRequires:	libxml2-devel
BuildRequires:	docbook2x
BuildRequires:	libevent-devel
BuildRequires:	opencv-devel >= 2.0
BuildRequires:	perl-devel
BuildRequires:	tokyocabinet-devel
BuildRequires:	protobuf-devel >= 2.4.0
BuildRequires:	protobuf-compiler

%description
Seeks is a free and open technical design that allows users to share their
queries to existing search engines. Its specific purpose is to regroup users
whose queries are similar so they can share both the query results and their
experience on these results. Applications and benefits are rather broad,
ranging from social websearch to dating and the building of communities based
on interests, professional activities, etc…

Seeks builds a social search overlay network and database on top
of the Internet and as thus includes many important features such as:

* Websites ratings, ranking and collaborative filtering,
* Query sharing and reuse of the experience of others,
* Discussion and comments on websites,
* Chat and discussion among search groups,
* Social monitoring of search group activity: you have access to the popularity
  of search queries in real time,
* Direct publishing system: the pushing of websites’ URL directly
  into the search groups through direct posting. This allows to get rid
  of crawlers and enables true real-time websearch.

%package -n %{libname}
Summary:	Seeks shared libraries
Group:		System/Libraries

%description -n %{libname}
This package contains shared libraries required for %{name}.

%package -n %{develname}
Summary:	Seeks development files
Group:		Development/C++
Requires:	%{libname} = %{version}

%description -n %{develname}
This package contains development files for %{name}.

%prep
%setup -q
%patch1 -p1 -b .cv

%build
%configure2_5x \
	--enable-static=no
make

%install
%makeinstall_std
install -D -m 755 %{SOURCE1} %{buildroot}%{_initddir}/%{name}
install -D -m 644 %{SOURCE2} %{buildroot}%{_sysconfdir}/%{name}/config
install -d -m 755 %{buildroot}%{_docdir}/%{name}
install -d -m 755 %{buildroot}%{_var}/lib/%{name}

%pre
%_pre_useradd seeks /var/empty /bin/false

%post
%_post_service %{name}

%preun
%_preun_service %{name}

%postun
%_postun_userdel seeks

%files
%{_bindir}/*
%{_libdir}/seeks/
%{_datadir}/seeks
%config(noreplace) %{_sysconfdir}/seeks
%{_mandir}/man1/seeks*
%{_initddir}/%{name}
%doc AGPL-3.txt AUTHORS BSD-yui.txt COPYING GPL-2.0.txt LGPL-2.1.txt README
%attr(-,seeks,seeks) %{_var}/lib/%{name}

%files -n %{libname}
%{_libdir}/*.so.%{major}*

%files -n %{develname}
%{_libdir}/*.so


%changelog
* Tue Apr 17 2012 Dmitry Mikhirev <dmikhirev@mandriva.org> 0.4.1-1
+ Revision: 791449
- update to 0.4.1

* Mon Feb 27 2012 Dmitry Mikhirev <dmikhirev@mandriva.org> 0.4.0-3
+ Revision: 781094
- added initscript
- various fixes from upstream

* Sat Feb 11 2012 Oden Eriksson <oeriksson@mandriva.com> 0.4.0-2
+ Revision: 773072
- relink against libpcre.so.1

* Tue Jan 31 2012 Dmitry Mikhirev <dmikhirev@mandriva.org> 0.4.0-1
+ Revision: 769993
- disabled SMP build
- fixed devel package requires
- use %%configure2_5x
- imported package seeks

