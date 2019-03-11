Name:       libsndfile
Summary:    Library for reading and writing sound files
Version:    1.0.28
Release:    1
Group:      System/Libraries
License:    LGPLv2+
URL:        http://www.mega-nerd.com/libsndfile/
Source0:    http://www.mega-nerd.com/libsndfile/files/libsndfile-%{version}.tar.gz
Patch0:     libsndfile-cmake-fix-man-pages.patch
Patch1:     libsndfile-cmake-target-name.patch
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig
BuildRequires:  cmake
BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(ogg)
BuildRequires:  pkgconfig(vorbis)
BuildRequires:  pkgconfig(flac)

%description
libsndfile is a C library for reading and writing sound files such as
AIFF, AU, WAV, and others through one standard interface. It can
currently read/write 8, 16, 24 and 32-bit PCM files as well as 32 and
64-bit floating point WAV files and a number of compressed formats. It
compiles and runs on *nix, MacOS, and Win32.

%package devel
Summary:    Development files for libsndfile
Group:      Development/Libraries
Requires:   %{name} = %{version}-%{release}

%description devel
libsndfile is a C library for reading and writing sound files such as
AIFF, AU, WAV, and others through one standard interface.
This package contains files needed to develop with libsndfile.

%package doc
Summary:    Documentation for %{name}
Group:      Documentation
Requires:   %{name} = %{version}-%{release}
Obsoletes:  %{name}-docs

%description doc
Man pages for %{name}.

%prep
%setup -q -n %{name}-%{version}/%{name}

%patch0 -p1
%patch1 -p1

%build

%cmake

make %{?_smp_mflags}

%install
rm -rf %{buildroot}
%make_install

mkdir -p %{buildroot}%{_docdir}/%{name}-%{version}
install -m0644 -t %{buildroot}%{_docdir}/%{name}-%{version} \
        AUTHORS README
mv %{buildroot}%{_docdir}/%{name} \
   %{buildroot}%{_docdir}/%{name}-%{version}/html

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%license COPYING
%{_bindir}/*
%{_libdir}/%{name}.so.*

%files devel
%defattr(-,root,root,-)
%{_includedir}/sndfile.h
%{_includedir}/sndfile.hh
%{_libdir}/%{name}.so
%{_libdir}/pkgconfig/sndfile.pc
%{_libdir}/cmake/%{name}/*.cmake

%files doc
%defattr(-,root,root,-)
%{_mandir}/man1/sndfile-*
%{_docdir}/%{name}-%{version}
