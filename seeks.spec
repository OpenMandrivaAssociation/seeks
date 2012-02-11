%define _disable_ld_no_undefined 1
%define _disable_ld_as_needed 1

%define major 0
%define libname %mklibname seeks %{major}
%define develname %mklibname seeks -d

Name:		seeks
Version:	0.4.0
Release:	2
Summary:	Open decentralized platform for collaborative search
Group:		Networking/WWW
License:	AGPLv3
URL:		http://www.seeks-project.info/
Source0:	http://www.seeks-project.info/site/releases/%{name}-%{version}.tar.gz
BuildRequires:	pcre-devel
BuildRequires:	curl-devel
BuildRequires:	libxml2-devel
BuildRequires:	docbook2x
BuildRequires:	libevent-devel
#BuildRequires:	opencv-devel >= 2.0
BuildRequires:	perl-devel
BuildRequires:	tokyocabinet-devel
BuildRequires:	protobuf-devel
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
Summary:        Seeks development files
Group:          Development/C++
Requires:	%{libname} = %{version}

%description -n %{develname}
This package contains development files for %{name}.

%prep
%setup -q

%build
%configure2_5x \
	--disable-opencv \
	--enable-static=no
make

%install
%makeinstall_std
install -d %{buildroot}%{_docdir}/%{name}

%files
%{_bindir}/*
%{_libdir}/seeks/
%{_datadir}/seeks
%config(noreplace) %{_sysconfdir}/seeks
%{_mandir}/man1/seeks*
%doc AGPL-3.txt AUTHORS BSD-yui.txt COPYING GPL-2.0.txt LGPL-2.1.txt NEWS README

%files -n %{libname}
%{_libdir}/*.so.%{major}*

%files -n %{develname}
%{_libdir}/*.so
