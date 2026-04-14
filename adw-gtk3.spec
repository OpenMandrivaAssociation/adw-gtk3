Name:           adw-gtk3
Version:        6.5
Release:        1
Summary:        The theme from libadwaita ported to GTK-3
BuildArch:      noarch

License:        LGPL-2.1-only
URL:            https://github.com/lassekongo83/adw-gtk3
Source0:        %{url}/releases/download/v%{version}/adw-gtk3v%{version}.tar.xz

%description
%{summary}.

%prep
%autosetup -c

%install
mkdir -p %{buildroot}%{_datadir}/themes
cp -ap adw-gtk3 %{buildroot}%{_datadir}/themes/adw-gtk3/
cp -ap adw-gtk3-dark %{buildroot}%{_datadir}/themes/adw-gtk3-dark/

%files
%{_datadir}/themes/adw-gtk3/
%{_datadir}/themes/adw-gtk3-dark/
