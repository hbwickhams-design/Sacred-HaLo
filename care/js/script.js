// Sacred HaLo Care & Referral Page JavaScript

// Configuration - UPDATE THESE WITH YOUR REAL INFO
const CONFIG = {
    baseUrl: 'https://sacredhaloconnection.com/care',
    
    // Contact information
    email: 'hello@sacredhalo.com',
    phone: '+15551234567',
    instagramHandle: 'sacredhaloconnection',
    
    // Booking
    bookingUrl: 'https://www.vagaro.com/sacredhalo',
    
    // Referral message template
    referralMessage: `✨ I just got permanent jewelry from Sacred HaLo and I think you'd love it! Use my link for $10 off your first piece: {{link}}\n\n"Welcomed. Seen. Understood. Connected."\n\n💎 @sacredhaloconnection`
};

// Referral System
const SacredHaloReferral = (function() {
    
    // Generate unique referral code for each customer
    function generateReferralCode() {
        // In a real implementation, this would be generated on the backend
        // For now, we'll use a simple timestamp-based code
        return 'SH-' + Date.now().toString(36).toUpperCase();
    }
    
    // Get or create referral link for this user
    function getReferralLink() {
        let referralCode = localStorage.getItem('sacredHaloReferralCode');
        
        if (!referralCode) {
            referralCode = generateReferralCode();
            localStorage.setItem('sacredHaloReferralCode', referralCode);
        }
        
        return `${CONFIG.bookingUrl}?ref=${referralCode}`;
    }
    
    // Format message with referral link
    function formatMessage() {
        const link = getReferralLink();
        return CONFIG.referralMessage.replace('{{link}}', link);
    }
    
    // Share via different platforms
    function shareReferral(platform) {
        const message = formatMessage();
        const link = getReferralLink();
        
        switch(platform) {
            case 'instagram':
                // Instagram doesn't have a direct sharing URL, so we copy to clipboard
                copyToClipboard(message);
                showNotification('Message copied! Open Instagram and paste in your story or DM 📷');
                // Optionally open Instagram
                window.open('https://www.instagram.com/' + CONFIG.instagramHandle, '_blank');
                break;
                
            case 'text':
                // SMS share (works on mobile)
                const smsBody = encodeURIComponent(message);
                window.location.href = `sms:?&body=${smsBody}`;
                break;
                
            case 'email':
                // Email share
                const emailSubject = encodeURIComponent('Check out Sacred HaLo! ✨');
                const emailBody = encodeURIComponent(message);
                window.location.href = `mailto:?subject=${emailSubject}&body=${emailBody}`;
                break;
                
            default:
                console.error('Unknown sharing platform:', platform);
        }
    }
    
    // Copy referral link to clipboard
    function copyLink() {
        const link = getReferralLink();
        copyToClipboard(link);
        showNotification('Link copied to clipboard! 🔗');
    }
    
    // Copy text to clipboard
    function copyToClipboard(text) {
        if (navigator.clipboard && navigator.clipboard.writeText) {
            navigator.clipboard.writeText(text).then(() => {
                console.log('Copied to clipboard successfully');
            }).catch(err => {
                console.error('Failed to copy:', err);
                fallbackCopy(text);
            });
        } else {
            fallbackCopy(text);
        }
    }
    
    // Fallback copy method for older browsers
    function fallbackCopy(text) {
        const textarea = document.createElement('textarea');
        textarea.value = text;
        textarea.style.position = 'fixed';
        textarea.style.opacity = '0';
        document.body.appendChild(textarea);
        textarea.select();
        
        try {
            document.execCommand('copy');
            console.log('Fallback copy successful');
        } catch (err) {
            console.error('Fallback copy failed:', err);
        }
        
        document.body.removeChild(textarea);
    }
    
    // Show notification toast
    function showNotification(message) {
        const notification = document.getElementById('notification');
        if (!notification) return;
        
        notification.textContent = message;
        notification.classList.add('show');
        
        setTimeout(() => {
            notification.classList.remove('show');
        }, 3000);
    }
    
    // Public API
    return {
        shareReferral,
        copyLink,
        showNotification
    };
})();

// Initialize when DOM is ready
document.addEventListener('DOMContentLoaded', function() {
    console.log('Sacred HaLo Care Page Loaded ✨');
    
    // Track referral if present in URL
    const urlParams = new URLSearchParams(window.location.search);
    const referralCode = urlParams.get('ref');
    
    if (referralCode) {
        console.log('Referral code detected:', referralCode);
        // In a real implementation, you would send this to your backend
        localStorage.setItem('incomingReferral', referralCode);
        SacredHaloReferral.showNotification('Welcome! You\'ve been referred by a friend 💚');
    }
});
