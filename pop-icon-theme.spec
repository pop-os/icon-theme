#
# Spec file for package pop-icon-theme
#
# Copyright (c) 2018 Sam Hewitt, 2019 Ian Santopietro, 2019 System76, Inc.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.
#

Name:           pop-icon-theme
Version:        0.1
Release:        0
License:        CC-BY-SA-4.0
Summary:        Pop Icon theme
Url:            https://github.com/pop-os/icon-theme
Group:          System/GUI/Other
Source:         %{name}-%{version}.tar.xz
BuildRequires:  automake
BuildRequires:  fdupes
BuildRequires:  hicolor-icon-theme
BuildRequires:  icon-naming-utils >= 0.8.7
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch

%description
Pop Icons are a simplistic icon theme fit to match the Pop theme, with 
architecture based on Sam Hewitt's Paper Icon Theme.

%prep
%setup -q
find -L . -type l -print -delete
chmod +x autogen.sh
chmod a-x AUTHORS README.md

%build
./autogen.sh
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot} %{?_smp_mflags}
rm -f %{buildroot}%{_datadir}/icons/Pop/AUTHORS
%fdupes %{buildroot}%{_datadir}/icons/Pop

%post
%icon_theme_cache_post Pop

%files
%defattr(-,root,root)
%doc AUTHORS COPYING LICENSE README.md
%{_datadir}/icons/Pop
%ghost %{_datadir}/icons/Pop/icon-theme.cache
