%include	/usr/lib/rpm/macros.perl
Summary:	Determine and mark up significant differences between latex files
Name:		latexdiff
Version:	1.0.4
Release:	1
License:	GPL v3
Group:		Applications
Source0:	http://dante.ctan.org/tex-archive/support/%{name}.zip
# Source0-md5:	40e076101b87e2334e20fa946b8a1607
Patch0:		%{name}-system-perl.patch
URL:		http://www.ctan.org/tex-archive/support/latexdiff/
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	unzip
Requires:	diffutils
Suggests:	texlive-latex-effects
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Latexdiff is a Perl script for visual mark up and revision of
significant differences between two latex files. Various options are
available for visual markup using standard latex packages such as
color . Changes not directly affecting visible text, for example in
formatting commands, are still marked in the latex source. A
rudimentary revision facilility is provided by another Perl script,
latexrevise, which accepts or rejects all changes. Manual editing of
the difference file can be used to override this default behaviour and
accept or reject selected changes only.

%prep
%setup -q -n %{name}
%patch0 -p1

%build

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1}
%{__make} install-fast \
	INSTALLPATH=$RPM_BUILD_ROOT%{_prefix} \
	INSTALLMANPATH=$RPM_BUILD_ROOT%{_mandir} \
	INSTALLEXECPATH=$RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/latex*.1.*
